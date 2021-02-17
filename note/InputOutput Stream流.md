# Input\Output Stream流

### java.io包

* 处理数据类型分类
  
  * 字符流：处理字符相关，如处理文本数据 Reader/Writer
  * 字节流：处理字节相关，如声音图片等二进制 InputStream/OutputStream
* 区别
  
  * 字节流以字节（8bit）为单位，字符流以字符为单位，根据码表映射字符，一次可能读多个字节
  * 字节流几乎可以处理所有文件，字符流只能处理字符类型数据

### InputStream

* InputStream是输入字节流的父类，它是一个抽象类（一般用它的子类）

```
    int read()
    讲解：从输入流中读取单个字节，返回0-255的int字节值，如果已经达到流末尾而没
    有可用的字节，则返回-1
    int read(byte [] buf)
    讲解：从输入流中读取一定数量的字节，并将其储存在缓冲区数组buf中，返回实际读取
    的字节数
    long skip(long n)
    讲解：从输入流中跳过并丢弃n个字节的数据
    int available()
    讲解：返回这个流中有多少个字节数，可以把buf长度定义为这个
    void close() throws IOExceptions
    讲解：关闭输入流并释放与该流关联的系统资源
    
```

* 常见子类
  
  * FileInputStream
    
    * 抽象类InputStream用来具体 实现类的创建对象，文件字节输入流，对文件数据以字节的形式进行读取操作
    * 常用构造函数
    
    ```
    //传入文件所在地址
    public FileInputStream(String name) throws FileNotFoundException
    //传入文件对象
    public FileInputStream(File file) throws FileNotFoundException
    
    
    
    ```

    ```
    
    ```

* ByteArrayInputStream
* ObjectInputStream
