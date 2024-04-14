import React, { useState } from 'react';
import { SafeAreaView, Text, TouchableOpacity, View, Alert } from 'react-native';
import tw from 'twrnc';
import axios from 'axios';
import StyledInput from '../../components/StyledInput';
import StyledButton from '../../components/StyledButton';
import BackButton from '../../components/BackButton';
import BackgroundImage from '../../components/BackgroundImage';

const ResetPasswordRequestScreen = ({ navigation }) => {
    const [email, setEmail] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleResetPassword = async () => {
        if (!email) {
            setErrorMessage('Please enter an email');
            return;
        }
    
        try {
            const response = await axios.post('http://127.0.0.1:8000/password-reset/', {
                email: email,
            });
    
            if (response.status === 200) {
                Alert.alert('Success', 'Reset link sent. Please check your email.');
            }
        } catch (error) {
            setErrorMessage('Failed to Send Reset Request');
        }
    };

    return (
        <SafeAreaView style={tw`flex-1 relative`}>
            <BackgroundImage />
            <View style={tw`w-full h-full z-50`} >
                <View style={tw`w-full h-[4rem] px-4`} >
                <BackButton onPress={() => navigation.goBack()} />
                </View>
                <View style={tw`w-full mt-[4rem] px-4`} >
                    <Text style={tw`text-[2.5rem] font-medium`}>Reset Password</Text>
                    <Text style={tw`text-[1.1rem] text-gray-700`}>
                        Enter your email to receive reset instructions
                    </Text>
                </View>

                <View style={tw`w-full mt-[6rem] px-4`} >
                    <StyledInput
                        placeholder="Email"
                        keyboardType="email-address"
                        value={email}
                        onChangeText={(text) => {setEmail(text) ; setErrorMessage(''); }} /> 
                </View>

                <View style={tw`w-full items-center`} >
                    {errorMessage? <Text style={tw`mt-4 text-red-500`}>{errorMessage}</Text> : null}
                    <StyledButton title="SEND RESET LINK" onPress={handleResetPassword} />
                </View>
            </View>
        </SafeAreaView>
    );
};

export default ResetPasswordRequestScreen;
