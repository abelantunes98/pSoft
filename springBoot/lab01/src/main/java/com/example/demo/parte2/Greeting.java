package com.example.demo.parte2;

public class Greeting {
	
	private String name;
	
	private String saudacao;
	
	public Greeting(String name, String saudacao) {
		this.setName(name);
		this.setSaudacao(saudacao);
	}
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSaudacao() {
		return saudacao;
	}

	public void setSaudacao(String saudacao) {
		this.saudacao = saudacao;
	}
	
}
