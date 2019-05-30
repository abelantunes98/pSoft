package service;

import org.springframework.stereotype.Service;

import dao.ProductDAO;
import model.Product;

@Service
public class ProductService {

	private  ProductDAO productDAO;
	
	ProductService(ProductDAO product) {
		this.productDAO = product;
	}
	
	public Product create(Product product) {
		return productDAO.save(product);
	}
	
	public Product update (Product productToUpdate) throws ProductNotFoundException {
		
		Product product = productDAO.findById(productToUpdate.getId());
		if (product == null) {
			throw new ProductNotFoundException("Could not update. The product not exist.");
		}
		
		return productDAO.save(productToUpdate);
	}
	
	public void delet(long id) {
		productDAO.deleteById(id);
	}
	
	public Product findById(long id) {
		return productDAO.findById(id);
	}

}