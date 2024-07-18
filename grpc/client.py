import grpc
import goods_pb2
import goods_pb2_grpc

def run():
    channel = grpc.insecure_channel('150.158.80.68:50051')
    stub = goods_pb2_grpc.GoodsInfoStub(channel)

    # Add goods
    goods = goods_pb2.Goods(
        name="python goods",
        description="a test sample",
        price=1200.00
    )
    response = stub.addGoods(goods)
    print("Added goods with ID:", response.id)

    # Get goods by ID
    goods_id = goods_pb2.GoodsId(id=response.id)
    response = stub.getGoodsById(goods_id)
    print("Goods ID:", response.id)
    print("Goods Name:", response.name)
    print("Goods Description:", response.description)
    print("Goods Price:", response.price)

if __name__ == '__main__':
    run()
