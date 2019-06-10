package com.abelantunes.backend2;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication(scanBasePackages={"com/rest/controller/", "com/rest/service", "com/rest/model"})
@ComponentScan("com/rest/controller/")

public class Backend2Application {

	public static void main(String[] args) {
		SpringApplication.run(Backend2Application.class, args);
		
	}

}
