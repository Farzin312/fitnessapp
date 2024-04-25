// Happiness.js
import React, { useState, useEffect } from 'react';
import { SafeAreaView, Text, View, Modal, TextInput, Alert, TouchableOpacity } from 'react-native';
import tw from 'twrnc';
import axios from 'axios';
import { useTheme } from '../../../components/ThemeContext';
import { DarkThemeComponents, LightThemeComponents } from '../../../components/ThemeComponents';
import HappinessGraph from './happinessgraph';

const Happiness = ({ navigation }) => {
    const [isModalVisible, setModalVisible] = useState(false);
    const [happinessRating, setHappinessRating] = useState('');
    const [happinessData, setHappinessData] = useState([]);
    const { isDarkTheme } = useTheme();
    const { ThemedText, SmallButton, Background, ModalView, TextInput, BackButton } = isDarkTheme ? DarkThemeComponents : LightThemeComponents;

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/user-aggregate/');
                if (Array.isArray(response.data)) {
                    setHappinessData(response.data);
                } else {
                    console.error('Data received is not an array:', response.data);
                }
            } catch (error) {
                console.error('Failed to fetch happiness data:', error);
            }
        };
        fetchData();
    }, []);

    const handleSaveHappiness = async () => {
        if (happinessRating.trim()) {
            try {
                const response = await axios.post('http://yourapi.com/happiness', { rating: parseInt(happinessRating, 10) });
                if (Array.isArray(response.data)) {
                    setHappinessData(response.data);
                } else {
                    setHappinessData([...happinessData, { rating: parseInt(happinessRating, 100) }]);
                }
                setHappinessRating('');
                setModalVisible(false);
                Alert.alert('Success', 'Happiness rating saved successfully');
            } catch (error) {
                Alert.alert('Error', 'Failed to save happiness rating');
            }
        }
    };

    return (
        <Background style={tw`w-full h-full`}>
            <SafeAreaView style={tw`flex-1`}>
                <View style={tw`w-full h-[4rem] px-4`}>
                    <BackButton onPress={() => navigation.goBack()} />
                </View>
                <View style={tw`p-4 justify-center items-center`}>
                    <ThemedText style={tw`text-2xl font-bold`}>Rate Your Happiness</ThemedText>
                    <SmallButton title="Rate Happiness" onPress={() => setModalVisible(true)} />
                </View>
                <Modal
                    animationType="slide"
                    transparent={true}
                    visible={isModalVisible}
                    onRequestClose={() => setModalVisible(false)}
                >
                    <View style={tw`flex-1 justify-center items-center bg-black bg-opacity-50`}>
                        <ModalView style={tw`m-4 p-4 bg-white rounded-lg shadow-lg w-11/12`}>
                            <Text style={tw`text-lg font-semibold`}>Enter your happiness rating (1-100):</Text>
                            <TextInput
                                style={tw`border border-gray-300 p-2 rounded mt-4`}
                                onChangeText={setHappinessRating}
                                value={happinessRating}
                                keyboardType="numeric"
                            />
                            <SmallButton title="Submit" onPress={handleSaveHappiness} />
                            <SmallButton title="Close" onPress={() => setModalVisible(false)} />
                        </ModalView>
                    </View>
                </Modal>
                {happinessData.length > 0 && <HappinessGraph data={happinessData} />}
            </SafeAreaView>
        </Background>
    );
};

export default Happiness;
