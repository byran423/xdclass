# 异常Exception

### 异常讲解

Java.lang软件包中有一个java.lang.Throwable类，这个类是Java中所有错误的超类，Throwable类有两个子类，Error和Exception

### Java内置异常

*Java内置异常

*     可查异常
  
  * ClassNotFoundException 应用程序试图加载类，找不到对应的类
  * IllegalAccessException拒绝访问一个类的时候
  * NoSuchFieldException 请求的变量不存在
  * NoSuchMethodException 请求的方法不存在
* 不可查异常
  
  * ArrayIndexOutOfBoundsException 数组索引越界
  * ClassCastException 强制失败抛出异常
  * NullPointException 需要对象的地方使用null时，抛出该异常
  * NumberFormatException 将字符串转换成一种数值类型，但该字符串不能转换为适当格式时抛出该异常

**finally最先执行，以finally返回结果为准**

### throw和throws

throws

* 声明异常，往外抛出
  
  * 语法：throws子句放在方法参数列表的右括号之后，一个方法可以声明抛出多个异常，多个异常之间用逗号隔开
  * 例子
    
    ```
    public class main(){
        public static void readChar() throws IOException,RemoteException{
            int input = System.in.read();
        }    
    }
    ```

try catch 中捕获了异常，处理方法

* 当前捕获自己处理
* 捕获自己处理然后继续往外面抛异常
  
  * 语法
    
    ```
    throw new ExceptionName("异常信息");
    ```
  * 例子
    
    ```
    throw new IOException("File not Found");
    ```
* 总结：当抛出一个被检查的异常，用try catch处理或者在方法声明中使用throws子句继续往外抛



### 自定义异常

```
public class BaseException extends Exception {
private String errorMessage;
 private String errorCode;
 public BaseException(String errorCode,String errorMessage){
 super(errorMessage);
 this.errorCode = errorCode;
 this.errorMessage = errorMessage;
 }
 public String getErrorMessage() {
 return errorMessage;
 }
 public String getErrorCode() {
 return errorCode;
 }
 public void setErrorCode(String errorCode) {
 this.errorCode = errorCode;
 }
 public void setErrorMessage(String errorMessage) {
 this.errorMessage = errorMessage;
 }
}
```


