package com.example.demo.parte2;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {
	
	@RequestMapping("/greeting")
	public Greeting greeting(@RequestParam(value="name", defaultValue="World") String name) {
		return new Greeting(name, saudacao());
	}
	
	public String saudacao() {
		String saudacao = "";
		LocalTime hora_atual = LocalTime.now();
		if(hora_atual.isBefore(LocalTime.NOON)) {
			saudacao = "bom dia";
		} else if (hora_atual.isAfter(LocalTime.NOON) && hora_atual.getHour() <= 18) {
			saudacao = "boa tarde";
		} else {
			saudacao = "boa noite";
		}
		return saudacao;
	}
	
	@RequestMapping("/greeting/time")
	public Time time() {
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
		String hora_atual = LocalTime.now().format(formatter);
		return new Time(hora_atual);
	}

}
