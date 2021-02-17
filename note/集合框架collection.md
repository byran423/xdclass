# 集合框架collection

****

### 数据结构

*按照数据的逻辑关系进行简单的分类，包括线型结构和非线型结构两类*

* 线型结构：各个结点具有线型关系，有且仅有一个开始点和终端结点
  
  * 栈、队列、和串
* 非线型结构：各个结点之间具有多个对应关系，一个结点可能有多个直接前趋结点和后续结点
  
  * 广义表、树结构、图结构



常见数据结构

* 栈
* 队列
* 数组
* 链表 Linked List
  
  * 数据元的素按照链式存储结构进行存储的数据结构，这种存储结构具有在物理上存在非连续的特点，每个数据节点包括数据域和指针域两部分。其中指针域保存了数据结构中下一个元素存放的地址

### 散列表Hash Table

什么是散列表

* 散列表（Hash Table 也叫哈希表），是根据关键码值（Key value）而直接进行访问的数据结构，也就是说，它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫做散列函数，存放记录的数组叫做散列
  
  给定表M，存在函数f(key)，对任意给定的关键字值key，代入函数后若能得到包含该关键字的记录在表中的地址，则称表M为哈希(Hash)表，函数f(key)为哈希(Hash)函数
  
  * 散列函数，能使对一个数据序列的访问过程更加迅速有效，通过散列函数，数据元素将被更快速的定位
* 链式哈希表
  
  * 是由一组链表组成，每个链表都可以看做是一个”桶“，我们将所有的元素通过散列的方式放到具体的不同的桶中。
  * 插入元素时，首先将其键传入一个哈希函数，函数通过散列的方式告知元素属于哪个”桶“，然后在响应的链表里插入元素。
  * 查找或者删除元素时，用同样的方式，先找到元素的”通“，然后遍历响应的链表，直到发现我们想要的元素。
* 注意：
  
  * 因为每个”桶“都是一个链表，如果表变得太大，它的性能同样将会降低
  * 哈希扩容：Bucket桶不够的话需要重新扩容，历史的数据需要重新hash
  * 哈希冲突碰撞：不同元素经过hash后命中相同的位置

### 什么是集合框架Collection

集合容器主要用于保存对象，主要分为三种：List，Set，Map

* List 有序、重复的集合
  
  * 常见的List有ArrayList，Vector,LinkedList等
* Set 无序，不可重复
  
  * 常见Set接口的实现类有HashSet，LinedHashSet,TreeSet这几类
* Map 键值对存储
  
  * 常见的Map接口实现类有HashMap和TreeSet

Collection接口有两个主要的子类List和Set，但Map不是collection的子类，因为其本身就是顶层接口

### List

常见的实现类

* ArrayList
  
  * 基于数组实现，是一个动态的数组队列，但它和Java中的数组又不一样，它的容量可以自动增长
  * 可以储存任意多的对象，但是只能储存对象，不能储存原生数据类型例如int
* LinkedList
  
  * 基于的数据结构是链表，一个双向链表，链表数据结构的特点是每个元素分配的空间不必连续
  * 插入和删除元素的速度非常快，但访问元素的速度较慢
* 常见List API语法
  
  ```
  list.add
  list.size
  list.remove(1)
  list.remove("jack")
  list.isEmpty
  list.get
  list.set
  list.clear
  ```
* LinkList特有API
  
  ```
  list.getFirst();
  list.getlast();
  ```

两者区别（常见面试题）

* 两个都是List接口，两个都是非线程安全的；
* ArrayList基于动态数组的数据结构，Linklist基于链表的数据结构；
* 对于随机访问get和set（查询操作），ArrayList要优于Linklist，因为Linklist要移动指针；
* 对于增删操作（add和remove），Linklist优于ArrayList；





### Map介绍

*什么是Map数据结构*

* 底层就是一个数组结构，数组中的每一项又是一个链表，即数组和链表的结合体；
* Table是数组，数组的元素是Entry；
* Entry元素是一个key-value键值对，它持有一个指向下一个Entry元素的引用，table数组的每个Entry元素同时也作为当前Entry链表的首节点，也指向该链表的下一个Entry元素

*常见的实现类*

* HashMap
  
  * 一个散列桶（组数和链表），它存储的内容是键值对（key-value)映射
  * 是基于hashing的原理，使用put（key,value)存储对象到HashMap中，使用get(key)从HashMap中获取对象。当put()方法传递键和值时，会先对键调用hashCode()方法，计算并返回的hashCode是用于找到Map数组的bucket位置来储存Entry对象的，是非线型安全的，所以HashMap操作速度很快
* TreeMap
  
  * 在数据的存储过程中，能够自动对数据进行排序，实现了SortedMap接口，它是有序的集合
  * TreeMap使用的存储结构是平衡二叉树，也称为红黑树
  * 默认排序规则：按照key的字典顺序来排序（升序），也可以自定义排序规则，要实现Comparator接口



*常见Map API语法*

```
HashMap<String,String> map = new HashMap<>();
        //TreeMap<String,String> map = new TreeMap<>();
        map.put("小明","广州");
        map.put("小红","上海");

        //返回所有value集合
        Collection<String> collection = map.values();
        System.out.println(collection);

        //返回所有key集合
        Set<String> set = map.keySet();
        System.out.println(set);

        //返回一个Set集合，集合的类型为Map.Entry,是Map声明的一个内部接口，接口为泛型，定义为Entry<k,v>
        //它表示Map中的一个实体(一个Key-value对)，主要有getKey(),getValue()防范
        Set<Map.Entry<String,String>> entrySet = map.entrySet();
        for (Map.Entry entry:entrySet){
            System.out.println("key= " + entry.getKey() +",values= " +  entry.getValue());


```





**Map面试题**

* HashMap和TreeMap怎么选择
  
  * HashMap可实现快速存储和检索，但缺点是包含的元素是无序的，适用于在Map中插入，删除和定位元素
  * TreeMap能便捷的实现对其内部元素的各种排序，但其性能比HashMap差，适用于按自然顺序或自定义顺序遍历键（key)
* jdk1.7和jdk1.8中HashMap的主要区别
  
  * 底层实现由之前的”数组+链表“改为”数组+链表+红黑树“
* 什么时候开始转变
  
  * 当链表节点较少时仍然以链表存在，当链表节点较多时，默认是大于**8**时，会转为红黑树，小于6时，重新变成链表



### Set介绍

*set数据结构*

* Set相对于List是简单的一种集合，具有和Collection完全一样的接口，只是实现上不同，Set不保存重复的元素，存储一组唯一，无序的对象。
* Set中元素不可以重复，实现细节可以参考Map，因为这些Set的实现都是对应的Map 的一种封装，比如HashSet是对HashMap的封装，TreeSet是对TreeMap的封装
* Set底层是一个HashMap，由于HashMap的put()方法是一个键值对，当新放入HashMap的Entry中key与集合中原有Entry的key相同（hashCode()返回值相等，通过equals比较也返回true），新添加的Entry的value将会覆盖原来的Entry的value值，但key不会有任何改变
* 允许包含为null的值，但最多只能有一个null元素

*常见的实现类*

* HashSet
  
  
* TreeSet

两者常见区别

* HashSet不能保证元素的排列顺序，TreeSet是SortedSet接口的唯一实现类，可以确保集合元素处于排序状态
* HashSet底层有的哈希表，TreeSet底层用的的红黑树
* HashSet中元素可以是null，但只能有一个，TreeSet不允许放入null
* 一般使用HashSet，如果需要排序的功能时，才使用TreeSet（性能原因）





### 集合框架拓展

*迭代器*

* 使用循环遍历集合
  
  * 普通for循环
    
    * for(int i;i<list.size(),i++){}
  * 增强for循环
    
    * for(String str :list){}
* 什么是迭代器
  
  * Iterator是Java中的一个接口，核心作用就是用来遍历容器元素，当容器实现了Iterator接口后，可以通过调用Iterator方法获取一个Iterator对象
  * 为啥是调用容器里面的Iterator方法呢？
    
    * 因为容器的实现有多种，不同的容器遍历规则不一样，比如ArrayList/LinkList/HashSet/TreeSet等，所以设计了Iterator接口，让容器本身去实现这个接口，实现里面的方法，从而让开发人员不用关心容器的遍历机制，直接使用对应的方法即可
  * 三个关键方法
    
    * Boolean hashNext()
      
      * 用于判断Iterator内是否有下个元素，如果有则返回true，没有则返回false
    * Object next()
      
      * 返回Iterator下一个元素，同时指针也会向后移动一位
    * void remove()
      
      * 删除指针的上一个元素（容易出问题，建议不使用容器自己的方法）
      * 只有当next执行完之后，才能调用remove函数
      * 如果删除第一个元素，不能直接调用remove(),要先next()一下，否则调用remove方法是会抛出异常的
  
  
  
  * 迭代器遍历元素时不能通过  Collection接口中的remove方法删除元素，只能用Iterator的remove方法删除元素，原因 某个线程Collection上进行迭代时，不允许另一个线程修改该Collection
  
  
* 和for循环对比
  
  * for循环适合顺序访问，或者通过下标进行访问的
  * 迭代器适合链式结构
  * 最终看使用场景，性能有轻微差别，可以忽略



### Collections工具类讲解

*Java里关于集合的工具类，包含有各种有关集合的静态多种方法，不能实例化（把构造函数私有化）*

*和Collection的区别*

* Collection是接口，提供了对集合进行基本操作的通用接口方法，List，Set等多种具体的实现类
* Collections是工具类，专门操作Collection接口实现类里面的元素

*获取最大元素 max(Collection coll)默认比较，不适合对象比较*
*获取最大元素max(Collection coll,Comparator comparator)*

*创建不可变集合unmodifiableXXX()*



### Comparable排序接口

*什么是Comparable*

```
public interface Comparable<T>{
    public int comparaTo(T,o);
}
```

* 是一个接口，定制排序规则
* 对实现它的每个类的对象进行整体排序，里面compareTo方法是实现排序的具体方法
* 比如TreeSet，SortedSet,Collection.sorted(),方法调用进行排序
* String，Integer,等类默认实现了这个接口，所以可以排序（看源码）



### Objects工具类

**Objects工具类讲解**

* jdk1.7引进的工具类，都是静态调用的方法，jdk1.8新增了部分方法
* 重点方法
  
  * equals
    
    * 用于字符串和包装对象的比较，先比较内存地址，再比较值
  * deepEquals
    
    * 数组的比较，先比较内存地址，再比较值，如String/Char/byte/int数组，或者包装类型integer等数组
  * hashCode
    
    * 返回对象的hashCode,若传入的为null，返回0
  * hash
    
    * 传入可变参数的所有值的hashCode的总和，底层调用Array.hashCode

**可变参数**只能在最后一个参数里面加

```
public static int hash(Object... values){
    return Array.hashCode(values);
}
```



### 新版JDK重写HashCode和Equals

**HashCode 和Equal方法**

* HashCode方法
  
  * 顶级类Object里面的方法，所有类都是继承Object的，返回值int类型
  * 根据一定的hash规则（储存地址，字段，或者长度等），映射成一个数值，即散列数值
* Equals方法
  
  * 顶级类Object里的方法，所有类都是继承Object的，返回值Boolean类型
  * 根据自定义的匹配规则，用于匹配两个对象是否一样，一般逻辑如下
    
    ```
    //判断地址是否一样
    //非空判断和class类判断
    //强转
    //对象里面的字段一一匹配
    ```
* 重写规则
  
  ```
  
      @Override
      public int hashCode() {
          return Objects.hash(name,age);
      }
  
      @Override
      public boolean equals(Object obj) {
          if (this == obj) return true;
          if (obj == null || getClass() == obj.getClass()) return false;
          User user = (User)obj;
          return age == user.age && name.equals(user.name);
  
      
  
      //IDE右键自动生成
  
  ```
  
  
* 问题：当向集合中插入对象时，如何判别在集合中是否已经存在该对象，比如Set确保存储对象的唯一，并判断是不是同个对象呢？
  
  * 根据hashCode和equals进行判断，所以Set存储的对象必须重写这两个方法
  * 判断两个对象是否一样，首先判断是否插入obj的hashCode值是否存在，hashCode值不存在则直接插入集合，值存在则还需用equals方法判断对象是否相等





### 作业

* 使用Collection来统计一段文字中每个字符出现的次数
  
  ```
  package chart9_9;
  
  import java.util.HashMap;
  import java.util.Map;
  import java.util.Set;
  
  public class QuestionTest {
  
      public static void main(String [] args){
          StringTestCount();
  
      }
  
      public static void StringTestCount(){
          String str = "lsjfljljsfjalflafalsfjl阿里附近加上放假ljfljalsjflajfljfljsajo按理说法阿斯蒂芬阿斯蒂" +
                  "芬阿斯蒂芬安抚垃圾射流风机dljldd大逻辑djjjjjjjjjjjdsdddddd";
  
          //把字符串转成数组
          char[] charArr = str.toCharArray();
          Map<Character,Integer> counterMap = new HashMap<>();
  
          //for循环遍历数组得到每个字符
          for (int i=0;i < charArr.length;i++){
              //拿到字符作为key去集合中查找
  
              Integer value = counterMap.get(charArr[i]);
              if (value == null){
                  //把字符作为key，1为值存储到集合
                  counterMap.put(charArr[i],1);
              }else {
                  //把值加1,重新写入集合
                  value +=1;
                  counterMap.put(charArr[i],value);
  
              }
  
              //遍历输出
              Set<Map.Entry<Character,Integer>> entrySet = counterMap.entrySet();
              for (Map.Entry<Character,Integer> entry : entrySet){
                  System.out.println(entry.getKey()+" 字符出现的字数为: "+entry.getValue());
              }
              System.out.println(entrySet);
  
  
          }
  
  
  
  
      }
  }
  
  ```
* A、B用户订单列表里面的交集（2种方式），差集（2种方式），并集，去重并集
  
  ```
   public static void main(String [] args){
          //StringTestCount();
          List<VideoOrder> videoOrders1 = new ArrayList<>();
          videoOrders1.add(new VideoOrder("a课程", 22));
          videoOrders1.add(new VideoOrder("w课程", 200));
          videoOrders1.add(new VideoOrder("c课程", 100));
          videoOrders1.add(new VideoOrder("d课程", 33));
          videoOrders1.add(new VideoOrder("f课程", 1));
  
  
          List<VideoOrder> videoOrders2 = new ArrayList<>();
          videoOrders2.add(new VideoOrder("a课程", 22));
          videoOrders2.add(new VideoOrder("b课程", 18));
          videoOrders2.add(new VideoOrder("d课程", 33));
          videoOrders2.add(new VideoOrder("f课程", 1));
          videoOrders2.add(new VideoOrder("z课程", 22));
  
          //交集
  //        videoOrders1.retainAll(videoOrders2);
  //        System.out.println(videoOrders1);
  
  
  //        List<VideoOrder> intersectionList = new ArrayList<>();
  //        for (VideoOrder videoOrder : videoOrders1){
  //            if (videoOrders2.contains(videoOrder)){
  //                intersectionList.add(videoOrder);
  //            }
  //        }
  //        System.out.println(intersectionList);
  
          //差集
  //        videoOrders1.removeAll(videoOrders2);
  //        System.out.println(videoOrders1);
  
  //        List<VideoOrder> diffList = new ArrayList<>();
  //        for (VideoOrder videoOrder : videoOrders1){
  //            if (!videoOrders2.contains(videoOrder)){
  //                diffList.add(videoOrder);
  //            }
  //        }
  //        System.out.println(diffList);
  //
  //        //并集
  //        videoOrders1.addAll(videoOrders2);
  //        System.out.println(videoOrders1);
  //
          //去重并集
          Set<VideoOrder> set = new HashSet<>(videoOrders1);
          System.out.println(videoOrders1);
  
  
  ```
  
  
