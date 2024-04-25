import React, { useState } from 'react';
import { SafeAreaView, Text, View, ScrollView } from 'react-native';
import tw from 'twrnc';
import { useTheme } from '../../components/ThemeContext';
import { DarkThemeComponents, LightThemeComponents } from '../../components/ThemeComponents';
import { AntDesign } from '@expo/vector-icons';

const Rankings =  ({navigation}) => {
    const { isDarkTheme, toggleTheme } = useTheme();
    const { ThemedText, BackButton, SmallButton, Background, Section, TouchOpacity } = isDarkTheme ? DarkThemeComponents : LightThemeComponents;

    return(
        <Background style={tw`w-full h-full z-50`} > 
            <SafeAreaView style={tw`flex-1 relative`}>
            <View style={tw`w-full h-[4rem] px-4`}>
                <BackButton onPress={() => navigation.goBack()} />
            </View>
            <View style={tw`p-4`}>
                <ThemedText style={tw`text-2xl font-bold`}>Profile</ThemedText>
            </View>
            <ScrollView style={tw`flex-1`} contentContainerStyle={tw`p-4`}>
            <View style={tw`flex-row flex-wrap justify-center`}>
                <TouchOpacity onPress={() => navigation.navigate('Happiness')}>
                    <AntDesign name="smileo" size={24} />
                    <Text>Happiness</Text>
                </TouchOpacity>
                <TouchOpacity onPress={() => navigation.navigate('Sleep')}>
                    <AntDesign name="eyeo" size={24} />
                    <Text>Sleep</Text>
                </TouchOpacity>
                <TouchOpacity onPress={() => navigation.navigate('Steps')}>
                    <AntDesign name="dashboard" size={24} />
                    <Text>Steps</Text>
                </TouchOpacity>
                <TouchOpacity onPress={() => navigation.navigate('Weight')}>
                    <AntDesign name="linechart" size={24} />
                    <Text>Weight</Text>
                </TouchOpacity>
            </View>
            </ScrollView>
            </SafeAreaView>
        </Background>
    );
};

export default Rankings;