import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import { TouchableOpacity } from 'react-native';

const SignupPage = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSubmit = () => {
    if (password !== confirmPassword) {
      Alert.alert("Password Mismatch", "The passwords do not match. Please try again.");
      return;
    }

    const url = 'http://127.0.0.1:8081/signUp';

    const formData = {
      firstName: firstName,
      lastName: lastName,
      email: email,
      username: username,
      password: password,
      confirmPassword: confirmPassword,
    };

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    };

    fetch(url, requestOptions)
      .then(response => {
        if (response.ok) {
          return response.json();
        } else if (response.status === 409) {
          Alert.alert("User Exists", "This username is already taken. Please choose another one.");
          return Promise.reject(new Error('User already exists'));
        } else {
          throw new Error('Network response was not ok.');
        }
      })
      .then(data => {
        console.log(data);
        Alert.alert("Success", "Form submitted successfully.");
      })
      .catch(error => {
        console.error('There was an error!', error);
        if (error.message !== 'User already exists') {
          Alert.alert("Network Error", "Failed to submit form. Please check your network connection and try again.");
        }
      });
  };

  return (
     <View style={styles.container}>
       <Text style={styles.title}>Sign Up</Text>
       <TextInput
         style={styles.input}
         placeholder="First Name"
       />
       <TextInput
         style={styles.input}
         placeholder="Last Name"
       />
       <TextInput
         style={styles.input}
         placeholder="Email"
         keyboardType="email-address"
       />
       <TextInput
         style={styles.input}
         placeholder="Username"
       />
       <TextInput
         style={styles.input}
         placeholder="Password"
         secureTextEntry
       />
       <TextInput
         style={styles.input}
         placeholder="Confirm Password"
         secureTextEntry
       />
       <TouchableOpacity style={styles.button} onPress={handleSubmit}>
         <Text style={styles.buttonText}>Sign Up</Text>
       </TouchableOpacity>
     </View>
   );
 };

 const styles = StyleSheet.create({
   container: {
     flex: 1,
     justifyContent: 'center',
     alignItems: 'center',
     paddingHorizontal: 20,
     backgroundColor: '#ffffff',
   },
   title: {
     fontSize: 24,
     fontWeight: 'bold',
     marginBottom: 20,
   },
   input: {
     width: '100%',
     height: 40,
     borderColor: '#cccccc',
     borderWidth: 1,
     borderRadius: 5,
     paddingHorizontal: 10,
     marginBottom: 10,
   },
   button: {
     width: '100%',
     height: 40,
     backgroundColor: '#007bff',
     justifyContent: 'center',
     alignItems: 'center',
     borderRadius: 5,
     marginTop: 10,
   },
   buttonText: {
     color: '#ffffff',
     fontSize: 16,
     fontWeight: 'bold',
   },
 });

export default SignupPage;
