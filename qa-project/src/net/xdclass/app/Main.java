package net.xdclass.app;

import net.xdclass.model.Response;
import net.xdclass.service.QkyRobotServicelmpl;
import net.xdclass.service.RobotService;

import java.util.Scanner;

public class Main {
    private static final RobotService robotService = new QkyRobotServicelmpl();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请给我取个名字,回车键结束");
        String name = scanner.nextLine();
        System.out.println("我是你的小助手,"+name+"请对我下达指令吧");
        while (true){
            String input = scanner.nextLine();
            if ("886".equalsIgnoreCase(input)){
                System.out.println("欢迎下次使用,再见");
                break;
            }else {
                Response response = robotService.qa(input);
                if (response!=null && response.getCode() == 0){
                    System.out.println(name+response.getContent());
                }else {
                    System.out.println(name+"暂时没明白您的意思");
                }
            }

        }
        scanner.close();


    }
}
