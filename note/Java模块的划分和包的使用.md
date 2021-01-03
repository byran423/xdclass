### Java模块的划分和包的使用

**  **

常见的Java自带的包

* java.lang 基础类包，默认自动导入的包，里面有Obect，String，StringBuffy，System等包，应用最广

* java.util 常见的工具类包

* java.io 提供系统的输入输出

* java.net 网络操作相关的包

作业：

```
import java.util.Random;

/**
 * 定义了一个Demo1类
 * @author yangbo
 * @version 1.0.0
 */
public class Demo1 {

    /*
    这是打印方法
     */
    public void firstcase(){
        System.out.println("这是第一个小程序");
    }

    public static void main(String [] args){
        Demo1 demo1 = new Demo1();
        demo1.firstcase();
        Random random = new Random();
        //随机生成true或者false
        System.out.println(random.nextBoolean());
        boolean flag = random.nextBoolean();
        System.out.println(flag);
    }
}

```


