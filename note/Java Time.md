# Java Time

JDK8之后，引入线程安全的日期和时间DateTimeFormatter

```
LocalDateTime ldt = LocalDateTime.now();
        System.out.println(ldt);
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String dtfstr = dtf.format(ldt);
        System.out.println(dtfstr);

```

时间差计算 java.time.Duration

```

```
