import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;

import java.awt.event.ActionEvent;
import java.awt.Color;
import java.awt.Font;
import javax.swing.JTextArea;
import javax.swing.JScrollBar;

public class myApplication {
	
	private JFrame frame;
	private JTextField textFieldName;
	private JLabel lblDisplayBoard;
	private JLabel lblID;
	private JTextField textFieldID;
	private JTextArea textDisplayArea;

	String message = "";
	private JScrollBar scrollBar;

	/**
	 * Launch the application.
	 */
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					myApplication window = new myApplication();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});		
	}

	/**
	 * Create the application.
	 */
	public myApplication() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame("Lab-11: Advanced Encryption Standard");
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		textFieldName = new JTextField();
		textFieldName.setBounds(139, 11, 194, 33);
		frame.getContentPane().add(textFieldName);
		textFieldName.setColumns(10);
		
		JLabel lblName = new JLabel("Enter Username");
		lblName.setBounds(10, 11, 119, 33);
		frame.getContentPane().add(lblName);
		
		JButton btnClickMe = new JButton("Click me");
		btnClickMe.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
				String userName = textFieldName.getText();
				String password = textFieldID.getText();
				textFieldName.setText("");
				textFieldID.setText("");
				
				//An object of AESTest is created here
				AES aet = new AES();
				
				
				try{
					byte[] plainText = userName.getBytes();
					byte[] cipherText = aet.encrypt(plainText);
					byte[] decryptedCipherText = aet.decrypt(cipherText);
				
					String displayDtring = "Username '"+userName+"' is encrypted to: "+new String(cipherText)+"\nThe decrypted Username: "+new String(decryptedCipherText);
					textDisplayArea.setText(displayDtring);
					
					plainText = password.getBytes();
					cipherText = aet.encrypt(plainText);
					decryptedCipherText = aet.decrypt(cipherText);
					
					displayDtring = displayDtring +"\n\n"+ "Password '"+password+"' is encrypted to: "+new String(cipherText)+"\nThe decrypted Password: "+new String(decryptedCipherText);
					textDisplayArea.setText(displayDtring);
				
				}catch(Exception e){
					System.out.println("Error message !");
				}
				
			}
		});
		btnClickMe.setBounds(145, 227, 89, 23);
		frame.getContentPane().add(btnClickMe);
		
		lblDisplayBoard = new JLabel("Eencrypted and decrypted message");
		lblDisplayBoard.setForeground(Color.RED);
		lblDisplayBoard.setFont(new Font("Tahoma", Font.BOLD, 12));
		lblDisplayBoard.setBounds(10, 94, 279, 23);
		frame.getContentPane().add(lblDisplayBoard);
		
		lblID = new JLabel("Enter Password");
		lblID.setBounds(10, 55, 119, 28);
		frame.getContentPane().add(lblID);
		
		textFieldID = new JTextField();
		textFieldID.setBounds(139, 55, 194, 28);
		frame.getContentPane().add(textFieldID);
		textFieldID.setColumns(10);
			
		JButton btnCancel = new JButton("Cancel");
		btnCancel.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		btnCancel.setBounds(244, 227, 89, 23);
		frame.getContentPane().add(btnCancel);
		
		textDisplayArea = new JTextArea();
		textDisplayArea.setForeground(Color.BLUE);
		textDisplayArea.setFont(new Font("Monospaced", Font.PLAIN, 14));
		textDisplayArea.setEditable(false);
		textDisplayArea.setBackground(Color.WHITE);
		textDisplayArea.setBounds(10, 116, 414, 100);
		frame.getContentPane().add(textDisplayArea);
		
		scrollBar = new JScrollBar();
		scrollBar.setBounds(216, 152, 17, 48);
		frame.getContentPane().add(scrollBar);
	}
}
