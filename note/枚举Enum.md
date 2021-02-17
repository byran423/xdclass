# 枚举Enum

* Java中的枚举Enum
  
  * 枚举类型是Java5中新增的特性，是一种特殊的数据类型
  * 定义枚举类型时使用的关键字enum，与class关键字类似，但前者是定义枚举类型，后者是定义类类型
  * 注意：
    
    * 枚举值一般是大写的字母，多个值之间以逗号分隔

```
package net.xdclass.chart15;

public class EnumTest {
    public static final int MONDAY = 1;
    public static final int TUESDAY = 2;
    public static final int WEDNESDAY= 3;
    public static final int THURSDAY = 4;
    public static final int FRIDAY = 5;
    public static final int SATURDAY = 6;
    public static final int SUNDAY = 7;

    public static void main(String[] args) {
        WeekEnum FRIDAY = WeekEnum.FRIDAY;
    }

}
enum WeekEnum{
    MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY
}
```



* 枚举常见API
  
  ```
  //返回枚举常量的名称
  name()
  
  
  //获取枚举变量在枚举类中声明的顺序，下标从0开始（它在枚举声明中的位置，其中
  初始常量序数为0，如果枚举的位置发生变化，对应的值也会变化）
  oridinal（）
  
  
  //和name方法一样
  toString（）
  ```

默认生成的value方法和valueOf方法

```
//通过字符串获取对应的枚举值
valueOf()


//获取枚举类中所有的变量，并作为数组返回
values()
```

* 例子
  
  ```
  WeekEnum [] week = WeekEnum.values();
          System.out.println(week);
          System.out.println(WeekEnum.values());
          for (WeekEnum  days:week){
              System.out.print(days+",");
  
  
          }
          System.out.println("------------");
          for (WeekEnum  days:week){
              System.out.print(days.name());
  
          }
  
          System.out.println(WeekEnum.valueOf("MONDAY"));
  ```
  
  
