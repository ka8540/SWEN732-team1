import React, { useState, useEffect } from 'react';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity, Alert } from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';

export default function Account({ navigation }) {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');

    useEffect(() => {
        // This should be replaced with your actual fetch call
        fetch('http://127.0.0.1:5000/userdetail')
            .then(response => response.json())
            .then(data => {
              if (data && data.length > 0) {
                const user = data[0]; // Access the first user details
                setFirstName(user.firstname);
                setLastName(user.lastname);
                setEmail(user.email);
                setUsername(user.username);
              }
            })
            .catch(error => {
                console.error('There was an error fetching the user details:', error);
            });
    }, []);

    const handleLogout = () => {
        Alert.alert(
            "Logout",
            "Are you sure you want to logout?",
            [
                {
                    text: "Cancel",
                    onPress: () => console.log("Cancel Pressed"),
                    style: "cancel"
                },
                { 
                    text: "Yes", onPress: () => {
                      console.log("Logout Pressed");
                      navigation.reset({
                        index: 0,
                        routes: [{ name: 'Login' }],
                      });
                    } 
                }
            ]
        );
    };

    return (
        <SafeAreaView style={styles.container}>
            {/* Navbar */}
            <View style={styles.navbar}>
                <Text style={styles.navbarText}>Account</Text>
            </View>

            {/* Main Content */}
            <View style={styles.content}>
                <MaterialCommunityIcons name="account-circle" size={100} color="black" />
                <Text style={styles.username}>{username}</Text>
                {/* Display additional account information here */}
                <Text style={styles.detailText}>First Name: {firstName}</Text>
                <Text style={styles.detailText}>Last Name: {lastName}</Text>
                <Text style={styles.detailText}>Email: {email}</Text>
            </View>

            {/* Logout Button */}
            <TouchableOpacity style={styles.button} onPress={handleLogout}>
                <Text style={styles.buttonText}>Logout</Text>
            </TouchableOpacity>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },
    navbar: {
        height: 60,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'cyan',
    },
    navbarText: {
        fontSize: 20,
        fontWeight: 'bold',
        color: '#fff',
    },
    content: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: 60, // Leave space for the logout button
    },
    username: {
        fontSize: 24,
        marginVertical: 20,
    },
    detailText: {
        fontSize: 18,
        marginVertical: 5,
    },
    button: {
        height: 60,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'navy',
    },
    buttonText: {
        fontSize: 20,
        color: '#fff',
        fontWeight: 'bold',
    },
});
