package com.rest.controller;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.rest.service.ProductService;
import com.exception.product.ProductNotFoundException;
import com.rest.model.Product;

@RestController
@RequestMapping({ "/v1/products" })
public class ProductController {

	private ProductService productService;

	public ProductController(ProductService productService) {
		this.productService = productService;
	}

	@GetMapping("/{id}")
	@ResponseBody
	public ResponseEntity<Product> findById(@PathVariable long id) {
		Product product = productService.findById(id);

		if (product == null) {
			throw new ProductNotFoundException("Product not found");
		}

		return new ResponseEntity<Product>(product, HttpStatus.OK);
	}
	
	@PostMapping(value = "/")
	@ResponseBody
	public ResponseEntity<Product> create(@RequestBody Product product  ) {
		Product newProduct = productService.create(product);

	    if (newProduct == null) {
	    //500?!?!
	    throw  new InternalError("Something went wrong");
	    }

	    return new ResponseEntity<Product>(newProduct, HttpStatus.CREATED);
	   }
/**	
	@GetMapping("/")
	public ResponseEntity<List<Product>> listall() {
		List<Product> products = productService.list();
		return new ResponseEntity<List<Product>>(products, HttpStatus.OK);
	}
**/	
	@DeleteMapping(value = "/{id}")
	   public ResponseEntity delete(@PathVariable long id) {
	       try {
	           productService.delete(id);
	           return new ResponseEntity(HttpStatus.OK);
	       } catch (Exception e) {
	           throw new InternalError("Something went wrong");
	       }
	   }



}
