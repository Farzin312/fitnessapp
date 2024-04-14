import React, { useState } from 'react';
import { SafeAreaView, Text, TouchableOpacity, View, ScrollView, TextInput, Alert } from 'react-native';
import tw from 'twrnc';
import axios from 'axios';
import DateTimePicker from '@react-native-community/datetimepicker';
import StyledInput from '../../components/StyledInput';
import StyledButton from '../../components/StyledButton';
import BackgroundImage from '../../components/BackgroundImage';
import StyledPicker from '../../components/StyledPicker';
import BackButton from '../../components/BackButton';

const RegisterScreen = ({ navigation }) => {
    const [date, setDate] = useState(new Date());
    const [mode, setMode] = useState('date');
    const [show, setShow] = useState(false);
    const [formattedDate, setFormattedDate] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [email, setEmail] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [sex, setSex] = useState('');
    const [secretQuestion, setSecretQuestion] = useState('');
    const [secretAnswer, setSecretAnswer] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const onChange = (_, selectedDate) => {
        const currentDate = selectedDate || date;
        setShow(false);
        setDate(currentDate);
        setFormattedDate(currentDate.toLocaleDateString());
    };
    
    const handleRegister = async () => {
        if (!username || !password || !confirmPassword || !email || !phoneNumber || !sex || !secretQuestion || !secretAnswer) {
            setErrorMessage('Please fill out all fields');
            return;
        }
    
        if (password !== confirmPassword) {
            setErrorMessage('Passwords do not match');
            return;
        }
    
        const convertDateFormat = (date) => {
            const [month, day, year] = date.split('/');
            let fullYear = year;
        
            if (year.length === 2) {
                fullYear = year.startsWith('9') ? `19${year}` : `20${year}`;
            }
        
            const formattedDay = day.padStart(2, '0');
            if (parseInt(formattedDay) < 1 || parseInt(formattedDay) > 31) {
                throw new Error('Invalid day in date');
            }
        
            return `${fullYear}-${month.padStart(2, '0')}-${formattedDay}`;
        };
    
        const payload = {
            user: {
                username: username,
                password: password,
                email: email,
                phone_number: phoneNumber,
            },
            secret_question: secretQuestion,
            secret_answer: secretAnswer,
            sex: sex,
            date_of_birth: convertDateFormat(formattedDate),
        };
    
        try {
            const response = await axios.post('http://127.0.0.1:8000/userprofiles/', payload);
    
            if (response.status === 201) {
                setErrorMessage('');
                Alert.alert('Successfully created user Account');
                navigation.navigate('LoginScreen');
            }
        } catch (error) {
            if (error.response) {
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                setErrorMessage(error.response.data.detail || 'Failed to create account');
            } else if (error.request) {
                console.log(error.request);
                setErrorMessage('No response from server');
            } else {
                console.log('Error', error.message);
                setErrorMessage('Error in request setup');
            }
        }
    };
    
         
      

    return (
        <SafeAreaView style={tw`flex-1 relative`}>
            <BackgroundImage />
            <ScrollView style={tw`flex-1`} contentContainerStyle={tw`items-center`}>
                <View style={tw`w-full h-full z-50 px-4`}>
                    <View style={tw`w-full h-[4rem]`}>
                    <BackButton onPress={() => navigation.goBack()} />
                    </View>
                    <View style={tw`w-full mt-4`}>
                        <Text style={tw`text-[2.5rem] font-medium`}>Welcome</Text>
                        <Text style={tw`text-[1.1rem] text-gray-700`}>Create Your Account</Text>
                    </View>

                    <View style={tw`w-full mt-6`}>
                        <StyledInput placeholder="Username" keyboardType="default" value={username} onChangeText={(text) => { setUsername(text); setErrorMessage(''); }} />
                        <StyledInput placeholder="Password" keyboardType="default" secureTextEntry={true} value={password} onChangeText={(text) => { setPassword(text); setErrorMessage(''); }}/>
                        <StyledInput placeholder="Confirm Password" keyboardType="default" secureTextEntry={true} value={confirmPassword} onChangeText={(text) => { setConfirmPassword(text); setErrorMessage(''); }} />
                        <StyledInput placeholder="Email" keyboardType="email-address" value={email} onChangeText={(text) => { setEmail(text); setErrorMessage(''); }}/>
                        <StyledInput placeholder="Phone Number" keyboardType="numeric" value={phoneNumber} onChangeText={(text) => { setPhoneNumber(text); setErrorMessage(''); }}/>
                        <TextInput
                            placeholder="Date of Birth (MM/DD/YYYY)"
                            value={formattedDate}
                            onChangeText={(text) => { setFormattedDate(text); setErrorMessage(''); }}
                            style={tw`bg-gray-200 p-3 rounded-lg mb-4`}
                        />
                        <TouchableOpacity onPress={() => setShow(true)} style={tw`bg-gray-200 p-3 rounded-lg mb-4`}>
                            <Text>Select Date of Birth</Text>
                        </TouchableOpacity>
                        {show && (
                            <DateTimePicker
                                testID="dateTimePicker"
                                value={date}
                                mode={mode}
                                is24Hour={true}
                                display="default"
                                onChange={(event, selectedDate) => { onChange(event, selectedDate); setErrorMessage(''); }}
                            />
                        )}
                        <StyledPicker
                            onValueChange= {(value) => { setSex(value); setErrorMessage(''); }}
                            items={[
                                { label: 'Male', value: 'male' },
                                { label: 'Female', value: 'female' },
                            ]}
                            placeholder={{ label: 'Select your Biological Sex', value: null }}
                        />
                        <StyledPicker
                            onValueChange={(value) => {
                                setSecretQuestion(value);
                                setErrorMessage('');
                            }}
                            items={[
                                { label: 'What is your mother\'s maiden name?', value: 'maiden_name' },
                                { label: 'What was the name of your first pet?', value: 'first_pet' },
                                { label: 'What was the make of your first car?', value: 'first_car' },
                                { label: 'What is your favorite color?', value: 'favorite_color' },
                                { label: 'In what city were you born?', value: 'birth_city' },
                            ]}
                            placeholder={{ label: 'Select a Secret Question', value: null }}
                        />
                        <StyledInput placeholder="Answer" keyboardType="default" value={secretAnswer} onChangeText={(text) => {setSecretAnswer(text); setErrorMessage(''); }}/>
                        <View style={tw`w-full items-center mt-4`}>
                        {errorMessage ? <Text style={tw`text-red-500 mb-4`}>{errorMessage}</Text> : null}
                            <StyledButton title="REGISTER" onPress= {handleRegister} />
                        </View>
                        <View style={tw`w-full items-center mt-4`}>
                        <TouchableOpacity onPress={() => navigation.navigate('LoginScreen')} style={tw`mt-4`}>
                            <Text style={tw`text-gray-600`}>Already have an account? Login</Text>
                        </TouchableOpacity>
                        </View>
                    </View>
                </View>
            </ScrollView>
        </SafeAreaView>
    );
};

export default RegisterScreen;