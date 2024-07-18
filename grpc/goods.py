from concurrent import futures
import grpc
import time

import goods_pb2
import goods_pb2_grpc

class GoodsInfoServicer(goods_pb2_grpc.GoodsInfoServicer):
    def __init__(self):
        self.goods_db = {}
        self.next_id = 1

    def addGoods(self, request, context):
        goods_id = self.next_id
        self.goods_db[goods_id] = {
            "name": request.name,
            "description": request.description,
            "price": request.price
        }
        self.next_id += 1
        return goods_pb2.GoodsId(id=goods_id)

    def getGoodsById(self, request, context):
        goods_id = request.id
        if goods_id in self.goods_db:
            goods = self.goods_db[goods_id]
            return goods_pb2.Goods(
                id=goods_id,
                name=goods["name"],
                description=goods["description"],
                price=goods["price"]
            )
        else:
            context.set_details("Goods not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return goods_pb2.Goods()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    goods_pb2_grpc.add_GoodsInfoServicer_to_server(GoodsInfoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
