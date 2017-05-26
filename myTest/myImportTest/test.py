import hello
import myTest.SayBye as sb  # 看起来如果使用test做包名会和什么东西发生冲突, 因此下次最好在python中test包一律叫做myTest
hello.sayHello()
sb.sayGoodBye()