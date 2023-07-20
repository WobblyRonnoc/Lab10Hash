import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class AES {
	
	private byte[] key = "12345678abcdefgh".getBytes();//This is your key
   

    public byte[] encrypt(byte[] plainText) throws Exception
    {
	//Put your code here


        return plainText;
    }

    /**
     *  Decrypts the given byte array
 		cipherText The data to decrypt
     */
    public byte[] decrypt(byte[] cipherText) throws Exception
    {
	//put your code here


        return cipherText;
    }


}
