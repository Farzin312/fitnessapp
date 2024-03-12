import React, { useState } from 'react';
import { SafeAreaView, Text, TouchableOpacity, View } from 'react-native';
import tw from 'twrnc';
import { AntDesign } from '@expo/vector-icons';
import StyledInput from '../../components/StyledInput';
import StyledButton from '../../components/StyledButton';
import BackgroundImage from '../../components/BackgroundImage';

const ResetPasswordScreen = ({ navigation }) => {
    const [email, setEmail] = useState('');

    const handleResetPassword = () => {
        // Call your API to reset the password
        // For example: resetPassword(email)
    };

    return (
        <SafeAreaView style={tw`flex-1 relative`}>
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
                        onChangeText={setEmail}
                    />
                </View>

                <View style={tw`w-full items-center`} >
                    <StyledButton title="SEND RESET LINK" onPress={handleResetPassword} />
                </View>
            </View>
        </SafeAreaView>
    );
};

export default ResetPasswordScreen;
