import React, { useState } from 'react';
import { SafeAreaView, Text, TouchableOpacity, View, ScrollView, TextInput } from 'react-native';
import tw from 'twrnc';
import axios from 'axios';
import { AntDesign } from '@expo/vector-icons';
import DateTimePicker from '@react-native-community/datetimepicker';
import StyledInput from '../../components/StyledInput';
import StyledButton from '../../components/StyledButton';
import BackgroundImage from '../../components/BackgroundImage';
import StyledPicker from '../../components/StyledPicker';

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
            return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
        };

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/userprofiles/', {
                username: username,
                password: password,
                email: email,
                phone_number: phoneNumber,
                secret_question: secretQuestion,
                secret_answer: secretAnswer,
                sex: sex,
                date_of_birth: convertDateFormat(formattedDate),
            });
    
            if (response.status === 201) {
                setErrorMessage('')
                navigation.navigate('LoginScreen');
            }
        } catch (error) {
            setErrorMessage('Failed to create account')
        }
    };

    return (
        <SafeAreaView style={tw`flex-1 relative`}>
            <BackgroundImage />
            <ScrollView style={tw`flex-1`} contentContainerStyle={tw`items-center`}>
                <View style={tw`w-full h-full z-50 px-4`}>
                    <View style={tw`w-full h-[4rem]`}>
                        <TouchableOpacity
                            activeOpacity={0.7}
                            style={tw`h-[3rem] w-[3rem] bg-gray-200 rounded-full items-center justify-center`}
                            onPress={() => navigation.goBack()}
                        >
                            <AntDesign name="arrowleft" size={24} color="black" />
                        </TouchableOpacity>
                    </View>

                    <View style={tw`w-full mt-4`}>
                        <Text style={tw`text-[2.5rem] font-medium`}>Welcome</Text>
                        <Text style={tw`text-[1.1rem] text-gray-700`}>Create Your Account</Text>
                    </View>

                    <View style={tw`w-full mt-6`}>
                        <StyledInput placeholder="Username" keyboardType="default" value={username} onChangeText={setUsername} />
                        <StyledInput placeholder="Password" keyboardType="default" secureTextEntry={true} value={password} onChangeText={setPassword}/>
                        <StyledInput placeholder="Confirm Password" keyboardType="default" secureTextEntry={true} value={confirmPassword} onChangeText={setConfirmPassword} />
                        <StyledInput placeholder="Email" keyboardType="email-address" value={email} onChangeText={setEmail}/>
                        <StyledInput placeholder="Phone Number" keyboardType="numeric" value={phoneNumber} onChangeText={setPhoneNumber}/>
                        <TextInput
                            placeholder="Date of Birth (MM/DD/YYYY)"
                            value={formattedDate}
                            onChangeText={setFormattedDate}
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
                                onChange={onChange}
                            />
                        )}
                        <StyledPicker
                            onValueChange= {setSex}
                            items={[
                                { label: 'Male', value: 'male' },
                                { label: 'Female', value: 'female' },
                            ]}
                            placeholder={{ label: 'Select your Biological Sex', value: null }}
                        />
                        <StyledPicker
                            onValueChange={setSecretQuestion}
                            items={[
                                { label: 'What is your mother\'s maiden name?', value: 'maiden_name' },
                                { label: 'What was the name of your first pet?', value: 'first_pet' },
                                { label: 'What was the make of your first car?', value: 'first_car' },
                                { label: 'What is your favorite color?', value: 'favorite_color' },
                                { label: 'In what city were you born?', value: 'birth_city' },
                            ]}
                            placeholder={{ label: 'Select a Secret Question', value: null }}
                        />
                        <StyledInput placeholder="Answer" keyboardType="default" value={secretAnswer} onChangeText={setSecretAnswer}/>
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