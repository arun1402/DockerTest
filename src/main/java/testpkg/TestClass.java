package testpkg;

import org.testng.annotations.Test;

public class TestClass {
  @Test
  public void FirstTest() {
	  
	  String os = System.getProperty("os.name").toLowerCase();
	  System.out.println("OS = " + os);
	  
  }
}
