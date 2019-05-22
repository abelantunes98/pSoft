package com.example.demo;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HelloController {
	
	@GetMapping("/hello")
	public String hello(@RequestParam(name="name", required=false, defaultValue="World") String name, Model model) {
		model.addAttribute("name", name);
		String saudacao = "";
		LocalTime hora_atual = LocalTime.now();
		if(hora_atual.isBefore(LocalTime.NOON)) {
			saudacao = "bom dia";
		} else if (hora_atual.isAfter(LocalTime.NOON) && hora_atual.getHour() <= 18) {
			saudacao = "boa tarde";
		} else {
			saudacao = "boa noite";
		}
		model.addAttribute("saudacao", saudacao);
		return "hello";
	}
	
	@GetMapping("/time")
	public String time(Model model) {
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
		String hora_atual = LocalTime.now().format(formatter);
		model.addAttribute("time", hora_atual);
		return "time";
	}

}
