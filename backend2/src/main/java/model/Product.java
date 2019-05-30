package model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import org.springframework.data.annotation.Id;

@Entity

public class Product {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private long id;
	
	private String name;
	private String description;
	private float price;
	
	public Product() {
		
	}
	
	public Product(String name, String description, float price) {
		this.name = name;
		this.description = description;
		this.price = price;
	}

	public void setName(String newName) {
		this.name = newName;
	}
	
	public void setDescription(String newDescription) {
		this.description = newDescription;
	}
	
	public void setPrice(float newPrice) {
		this.price = newPrice;
	}
	
	public long getId() {
		return this.id;
	}
	
	public String getName() {
		return this.name;
	}
	
	public String getDescription() {
		return this.description;
	}
	
	public float getValue() {
		return this.price;
	}
}
