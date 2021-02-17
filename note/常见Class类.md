# 常见Class类

#### Java顶级对象 Object对象  --面试题

* Object类位于java.lang包中，java.lang包包含着Java最基础和核心的类，在编译时会自动导入
* Object类是所有Java类的祖先，每个类都会使用Object作为超类
* 常见方法
  
  ```
  public final native Class<?> getClass()
  讲解：获取对象的运行时class对象，class对象就是描述对象所属类的对象，类的对象可以获取这个类的基本信息
  如：名、包、字段、方法等（用于反射会比较多）
  
  
  public native int hashCode()
  讲解：获取对象的散列值，集合框架中应用，比如HashMap
  
  
  public boolean equals(Object obj)
  讲解：比较两个对象，如果这两个对象的引用指向的是同一个对象，那么返回ture，否则返回flase
  
  public String toString（）
  讲解：用于返回一个可代表对象的字符串，看源码可以得知，默认返回格式如下，对象的class名称+@+hashCode
  的十六进制字符串，方便调试
  ```
* native方法，本地方法，具体是用C(C++)在DLL中实现的，然后在JNI调用
* 什么是JNI：Java平台和本地C(C++)代码进行互操作的API，称为Java Native Interface（Java本地接口）
  
  ### 
  
  
  
  
  
  

### Math类

* 什么是Math类
  
  * Java操作数学运算相关的类
  * 构造函数被私有化，所以不允许创建对象
  * 都是静态方法，直接使用类名+方法名
* 常用API
  
  ```
  
  ```
* Math.random()产生0~1 的随机数





### String进阶

* 常用API
  
  ```
          boolean bool = Boolean.getBoolean("flase");
          int integer = Integer.parseInt("20");
          long longInt = Long.parseLong("2000");
          double d = Double.parseDouble("20.01");//双精度
          float f = Float.parseFloat("20.01");//单精度
  ```



### System 类

```
        System.out.println(System.currentTimeMillis());
        System.out.println(System.getProperties());
        System.out.println(System.getProperty("os.name"));

```



### 基本数据类型对应的包装类型

* 什么是包装数据类型
  
  * Java是一个面向对象的语言，但基本类型不具有对象的性质，为了让基本类型也具有对象的特征，就出现了包装类型
    
    * 集合框架里需要储存对象，不能储存基本数据类型，所以需要储存包装类型
* Java里的包装数据类型
  
  ```
  基本类型    包装类型
  boolean    Boolean
  char       Character
  int        Integer
  byte       Byte
  short      Short
  long       Long
  float      Float
  double     Double
  ```
* 相互转换
  
  ```
          int i1 = 0;
          Integer integer1 = new Integer(i1);
          int i2 = integer1.intValue();
          System.out.println(i1);
          System.out.println(integer1);
          System.out.println(i2);
  ```
* 基本数据类型和包装数据类型的区别
  
  * 基本数据类型不用new，包装类型需要用new关键字来在堆中分配存储空间
  * 存储方式及位置不同，基本类型是直接将变量的值存储在栈中，包装类型是将对象放在堆中，然后通过引用来使用
  * 初始值不同，基本数据类型的初始值如int为0，boolean为flase，包装类型的初始值为null
