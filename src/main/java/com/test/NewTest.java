package com.test;

import org.testng.annotations.Test;

public class NewTest {

    @Test
    public void FindOS() {
    	
    	String os = System.getProperty("os.name").toLowerCase();
    	System.out.println("OS = " + os);

    }
}

