import React, { useState } from 'react';
import { SafeAreaView, Text, View, ScrollView } from 'react-native';
import tw from 'twrnc';
import { useTheme } from '../../components/ThemeContext';
import { DarkThemeComponents, LightThemeComponents } from '../../components/ThemeComponents';

const Settings = ({ navigation }) => {
    const { isDarkTheme, toggleTheme } = useTheme();
    const { ThemedText, ToggleThemeButton, BackButton, SmallButton, Background, Section } = isDarkTheme ? DarkThemeComponents : LightThemeComponents;

    const handleLogout = () => {
        navigation.navigate('LoginScreen');
    };

    return (
       <Background style={tw`w-full h-full z-50`} > 
       <SafeAreaView style={tw`flex-1 relative`}>          
            <View style={tw`w-full h-[4rem] px-4`}>
                <BackButton onPress={() => navigation.goBack()} />
            </View>
            <View style={tw`p-4`}>
                <ThemedText style={tw`text-2xl font-bold`}>Settings</ThemedText>
            </View>
            <ScrollView style={tw`flex-1`} contentContainerStyle={tw`p-4`}>
            
            <Section title="Dark Mode" description="Adjust the theme of the application.">
               <ToggleThemeButton isDarkTheme={isDarkTheme} onToggle={toggleTheme} />          
            </Section>                   
            
            <Section title="Logout" description="">
                <SmallButton title="Logout" onPress={handleLogout} />
            </Section>                      
            </ScrollView>  
        </SafeAreaView> 
        </Background>
    );
};

export default Settings;     
                    
                    
                       
            
