import React from 'react';
import { SafeAreaView, Text, TouchableOpacity, View } from 'react-native';
import tw from 'twrnc';
import { AntDesign } from '@expo/vector-icons';
import StyledInput from '../../components/StyledInput';
import StyledButton from '../../components/StyledButton';
import BackgroundImage from '../../components/BackgroundImage';

const LoginScreen = ({navigation}) => {
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
          />
          <StyledInput
            placeholder='Password'
            keyboardType='default'
            secureTextEntry={true}
          />
        </View>

        <View style={tw`w-full items-center`}>
          <StyledButton title="LOGIN" onPress={() => {/* Handle login */}} />
          <TouchableOpacity onPress={() => navigation.navigate('ResetPasswordScreen')}>
          <Text style={tw`mt-4 text-gray-600`}>Forgotten Password</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={() => navigation.navigate('RegisterScreen')}>
            <Text style={tw`mt-4 text-gray-600`}>Or Create a New Account</Text>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
};

export default LoginScreen;
