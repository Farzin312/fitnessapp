import React, { useState } from 'react';
import { SafeAreaView, Text, TouchableOpacity, View, ActivityIndicator } from 'react-native';
import tw from 'twrnc';
import axios from 'axios';
import { AntDesign } from '@expo/vector-icons';
import StyledInput from '../../components/StyledInput';
import StyledButton from '../../components/StyledButton';
import BackgroundImage from '../../components/BackgroundImage';

const LoginScreen = ({navigation}) => {

    const [loginInput, setLoginInput] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [loading, setLoading] = useState(false);
    
    const handleLogin = async () => {
        try {
        const response = await axios.post('http://127.0.0.1:8000/login/', 
        {
            login_input: loginInput,
            password: password
        });
        setLoading(false);
        const token = response.data.token;
        navigation.navigate('MainPage', {token: token, loginInput: loginInput })
    }  catch (error) {
        if (error.response && error.response.status === 400) {
            setErrorMessage('Invalid username/email or password.');
        } else {
            setErrorMessage('An error occurred. Please try again.');
        }
    }
};

  return (
    <SafeAreaView style={tw`flex-1 relative`} >
      <BackgroundImage />
      <View style={tw`w-full h-full z-50`} >
        <View style={tw`w-full h-[4rem] px-4`} >
          <TouchableOpacity activeOpacity={.7} 
            style={tw`h-[3rem] w-[3rem] bg-gray-200 rounded-full items-center justify-center`}
            onPress={() => navigation.goBack()}
          >
            <AntDesign name="arrowleft" size={24} color="black" />
          </TouchableOpacity>
        </View>

        <View style={tw`w-full mt-[4rem] px-4`} >
          <Text style={tw`text-[2.5rem] font-medium`}>
            Welcome Back
          </Text>
          <Text style={tw`text-[1.1rem] text-gray-700`}>
            Enter Your Username or Email & Password
          </Text>
        </View>

        <View style={tw`w-full mt-[6rem] px-4`} >
          <StyledInput
            placeholder='Username or Email'
            keyboardType='default'
            value={loginInput}
            onChangeText={(text) => {
            setLoginInput(text);
            setErrorMessage('');
            }}
          />
          <StyledInput
            placeholder='Password'
            keyboardType='default'
            secureTextEntry={true}
            value={password}
            onChangeText={(text) => {
            setPassword(text);
            setErrorMessage('');
            }}
          />
        </View>

        <View style={tw`w-full items-center`}>
            {loading ? ( <ActivityIndicator size="large" color="#0000ff" />
            ): (
            <>
          <StyledButton title="LOGIN" onPress= {handleLogin} />
          {errorMessage ? <Text style={tw`mt-4 text-red-500`}>{errorMessage}</Text> : null}
          <TouchableOpacity onPress={() => navigation.navigate('ResetPasswordScreen')}>
          <Text style={tw`mt-4 text-gray-600`}>Forgotten Password</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={() => navigation.navigate('RegisterScreen')}>
            <Text style={tw`mt-4 text-gray-600`}>Or Create a New Account</Text>
          </TouchableOpacity>
          </>
            )}
        </View>
      </View>
    </SafeAreaView>
  );
};

export default LoginScreen;
