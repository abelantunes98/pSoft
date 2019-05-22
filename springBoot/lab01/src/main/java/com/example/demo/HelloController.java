package com.example.demo;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

/*
 * Classe de redirecionamento para o "sistema" hello
 * - Recebe o path desejado e redireciona para a pagina requisitada
 * ou para uma pagina de erro, caso o path nao exista.
 */
@Controller
public class HelloController {
	
	/*
	 * Metodo para o path hello, caso o path digitado seja /hello
	 */
	@GetMapping("/hello")
	public String hello(@RequestParam(name="name", required=false, defaultValue="Friend") String name, Model model) {
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
	
	/**
	 * Retorna a pagina time caso o path informnado seja /time
	 */
	@GetMapping("/time")
	public String time(Model model) {
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
		String hora_atual = LocalTime.now().format(formatter);
		model.addAttribute("time", hora_atual);
		return "time";
	}
	
	@RequestMapping(value="/{path}", method=RequestMethod.GET)
	public String errorPage (@PathVariable("path") String path) {
		
		String caminhos = "hello time timeJson";
		if (!caminhos.contains(path)) {
			return "error";
		}
		
		else if (path.equals("hello")) {
			return "redirect:/hello";
		}
		
		else if (path.equals("time")) {
			return "redirect:/time";
		}
		
		else {
			return "error";
		}
	}
	
}
