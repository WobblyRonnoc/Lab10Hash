/*
 *File checksum with MD5
* It will use MD5 hashing algorithm to generate a checksum for a zip file in c:\MD5_test\test.zip.
 */
import java.io.*;
import java.security.MessageDigest;

public class MD5 {

	public static void main(String[] args)throws Exception {
		MessageDigest md = MessageDigest.getInstance("MD5");
        	FileInputStream fis = new FileInputStream("c:\\Lab-11\\test.zip");
        	byte[] dataBytes = new byte[1024];
       	 	int nread = fis.read(dataBytes);
        	md.update(dataBytes, 0, nread);   
        	byte[] mdbytes = md.digest();

        	//convert the byte to hex format method 1
        	StringBuffer sb = new StringBuffer();
        	for (int i = 0; i < mdbytes.length; i++) {
          		sb.append(Integer.toString((mdbytes[i] & 0xff) + 0x100, 16).substring(1));
        	}

        	System.out.println("Digest(in hex format):: " + sb.toString());

	}//end main
}//end class
