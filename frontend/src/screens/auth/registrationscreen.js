import React, { useState } from 'react';
import { SafeAreaView, Text, TouchableOpacity, View, ScrollView, TextInput } from 'react-native';
import tw from 'twrnc';
import { AntDesign } from '@expo/vector-icons';
import RNPickerSelect from 'react-native-picker-select';
import DateTimePicker from '@react-native-community/datetimepicker';
import StyledInput from '../../components/StyledInput';
import StyledButton from '../../components/StyledButton';
import BackgroundImage from '../../components/BackgroundImage';

const RegisterScreen = ({ navigation }) => {
    const [date, setDate] = useState(new Date());
    const [mode, setMode] = useState('date');
    const [show, setShow] = useState(false);
    const [formattedDate, setFormattedDate] = useState('');

    const onChange = (_, selectedDate) => {
        const currentDate = selectedDate || date;
        setShow(false);
        setDate(currentDate);
        setFormattedDate(currentDate.toLocaleDateString());
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
                        <StyledInput placeholder="Username" keyboardType="default" />
                        <StyledInput placeholder="Password" keyboardType="default" secureTextEntry={true} />
                        <StyledInput placeholder="Confirm Password" keyboardType="default" secureTextEntry={true} />
                        <StyledInput placeholder="Email" keyboardType="email-address" />
                        <StyledInput placeholder="Phone Number" keyboardType="numeric" />
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
                        <RNPickerSelect
                            onValueChange={(value) => console.log(value)}
                            items={[
                                { label: 'Male', value: 'male' },
                                { label: 'Female', value: 'female' },
                            ]}
                            placeholder={{ label: 'Select your Biological Sex', value: null }}
                            style={{ inputAndroid: { color: 'black' } }}
                        />
                        <RNPickerSelect
                            onValueChange={(value) => console.log(value)}
                            items={[
                                { label: 'What is your mother\'s maiden name?', value: 'maiden_name' },
                                { label: 'What was the name of your first pet?', value: 'first_pet' },
                                { label: 'What was the make of your first car?', value: 'first_car' },
                                { label: 'What is your favorite color?', value: 'favorite_color' },
                                { label: 'In what city were you born?', value: 'birth_city' },
                            ]}
                            placeholder={{ label: 'Select a Secret Question', value: null }}
                            style={{ inputAndroid: { color: 'black' } }}
                        />
                        <StyledInput placeholder="Answer" keyboardType="default" />
                        <View style={tw`w-full items-center mt-4`}>
                            <StyledButton title="REGISTER" onPress={() => {/* Handle registration */}} />
                        </View>
                    </View>
                </View>
            </ScrollView>
        </SafeAreaView>
    );
};

export default RegisterScreen;
