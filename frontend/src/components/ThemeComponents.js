import React from 'react';
import { TouchableOpacity, Text, View, Switch } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import tw from 'twrnc';

const CommonComponents = {
    Background: ({ children, style }) => (
        <View style={[tw`flex-1`, style]}>
            {children}
        </View>
    ),
    
    TouchOpacity: ({ onPress, style, children }) => (
        <TouchableOpacity 
            onPress={onPress} 
            style={[tw`flex-row items-center justify-center p-4 rounded-lg shadow m-1`, style]}>
            {children}
        </TouchableOpacity>
    ),

    BackButton: ({ onPress, style }) => (
        <TouchableOpacity 
            activeOpacity={0.7} 
            onPress={onPress} 
            style={[tw`h-[3rem] w-[3rem] rounded-full items-center justify-center`, style.button]}
        >
            <AntDesign name="arrowleft" size={24} color={style.iconColor} />
        </TouchableOpacity>
    ),

    SmallButton: ({ title, onPress, style }) => (
        <TouchableOpacity 
            onPress={onPress} 
            style={[tw`rounded-lg py-2 px-4 mt-1`, style.button]}>
            <Text style={[tw`text-center`, style.text]}>{title}</Text>
        </TouchableOpacity>
    ),

    Section: ({ title, description, style, children }) => (
        <View style={[tw`p-4 rounded-lg shadow mt-4`, style.container]}>
            <Text style={[tw`text-lg font-semibold`, style.title]}>{title}</Text>
            <Text style={[tw`text-sm`, style.description]}>{description}</Text>  
            {children}
        </View>
    ),

    ToggleThemeButton: ({ isDarkTheme, onToggle }) => (
        <Switch
            trackColor={{ false: tw`color-gray-200`, true: tw`color-gray-800` }}
            thumbColor={isDarkTheme ? tw`color-white` : tw`color-black`}
            ios_backgroundColor={tw`color-gray-200`}
            onValueChange={onToggle}
            value={isDarkTheme}
        />
    ),

    TextInput: ({ style, ...props }) => (
        <TextInput
            style={[tw`border p-2 rounded mt-2`, style]}
            {...props}
        />
    ),
    ModalView: ({ style, children }) => (
        <View style={[tw`p-4 rounded-lg shadow`, style]}>
            {children}
        </View>
    ),
};

const DarkThemeComponents = {
    ...CommonComponents,
    Background: props => CommonComponents.Background({
        ...props, style: { backgroundColor: '#333', ...props.style }
    }),
    
    BackButton: props => CommonComponents.BackButton({
        ...props, style: { button: tw`bg-gray-800`, iconColor: 'white' }
    }),

    SmallButton: props => CommonComponents.SmallButton({
        ...props, style: { button: tw`bg-black`, text: tw`text-white` }
    }),

    Section: props => CommonComponents.Section({
        ...props,
        style: {
            container: tw`bg-gray-600`,
            title: tw`text-white`,
            description: tw`text-gray-300`
        }
    }),
    ToggleThemeButton: props => CommonComponents.ToggleThemeButton({
        ...props, isDarkTheme: true
    }),

    TextInput: props => CommonComponents.TextInput({
        ...props, style: tw`bg-gray-800 text-white border-gray-600`
    }),
    ModalView: props => CommonComponents.ModalView({
        ...props, style: tw`bg-gray-800`
    }),
    TouchOpacity: props => CommonComponents.TouchOpacity({
        ...props, style: tw`bg-gray-600 text-white`
    }),

};

const LightThemeComponents = {
    ...CommonComponents,
    Background: props => CommonComponents.Background({
        ...props, style: { backgroundColor: '#f9edcc', ...props.style }
    }),
    
    BackButton: props => CommonComponents.BackButton({
        ...props, style: { button: tw`bg-[rgba(237,174,73,1)]`, iconColor: 'black' }
    }),

    SmallButton: props => CommonComponents.SmallButton({
        ...props, style: { button: tw`bg-[rgba(237,174,73,1)]`, text: tw`text-black` }
    }),

    Section: props => CommonComponents.Section({
        ...props,
        style: {
            container: tw`bg-[rgba(249,223,116,1)]`,
            title: tw`text-black`,
            description: tw`text-gray-800`
        }
    }),

    ToggleThemeButton: props => CommonComponents.ToggleThemeButton({
        ...props, isDarkTheme: false
    }),

    TextInput: props => CommonComponents.TextInput({
        ...props, style: tw`bg-white text-black border-gray-300`
    }),
    ModalView: props => CommonComponents.ModalView({
        ...props, style: tw`bg-white`
    }),
    TouchOpacity: props => CommonComponents.TouchOpacity({
        ...props, style: tw`bg-[rgba(249,223,116,1)]`
    }),
};

export { DarkThemeComponents, LightThemeComponents };
