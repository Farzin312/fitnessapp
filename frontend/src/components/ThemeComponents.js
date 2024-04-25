import React from 'react';
import { TouchableOpacity, Text, View, Switch, TextInput as RNTextInput } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import tw from 'twrnc';

const CommonComponents = {
    Background: ({ children, style }) => (
        <View style={[tw`flex-1`, style]}>
            {children}
        </View>
    ),
    
    ThemedText: ({ children, style, ...props }) => (
        <Text style={[style, props]}>{children}</Text>
    ),
      
   
    TouchOpacity: ({ onPress, style = {}, children }) => (
        <TouchableOpacity 
            onPress={onPress} 
            style={[tw`w-1/2.5 h-30 justify-center items-center rounded-lg shadow-lg m-1`, style]}>
            {React.Children.map(children, child => {
                if (React.isValidElement(child)) {
                    let extraProps = {};
                    if (child.type === Text) {
                        extraProps = { style: [{ color: style.textColor || 'inherit' }, ...(child.props.style || [])] };
                    }
                    else if (child.type === AntDesign || (child.type.displayName && child.type.displayName === 'AntDesign')) {
                        extraProps = { color: style.iconColor || 'inherit' };
                    }
                    return React.cloneElement(child, extraProps);
                }
                return child;
            })}
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
            trackColor={{ false: "#d1d5db", true: "#1f2937" }} 
            thumbColor={isDarkTheme ? "#ffffff" : "#EDAE49"} 
            ios_backgroundColor="#ffffff" 
            onValueChange={onToggle}
            value={isDarkTheme}
        />
    ),

    TextInput: ({ style, ...props }) => (
        <RNTextInput
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

    ThemedText: props => CommonComponents.ThemedText({
        ...props, style: { color: 'white', ...props.style }
    }),
    
    BackButton: props => CommonComponents.BackButton({
        ...props, style: { button: tw`bg-gray-800`, iconColor: 'white' }
    }),

    SmallButton: props => CommonComponents.SmallButton({
        ...props, style: { button: tw`bg-black`, text: tw`text-white` }
    }),

    Section: props => CommonComponents.Section({
        ...props, style: { container: tw`bg-gray-600`,title: tw`text-white`,description: tw`text-gray-300` }
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
        ...props, style: { ...tw`bg-gray-600`, textColor: 'white', iconColor: 'white', ...props.style }
    }),

};


const LightThemeComponents = {
    ...CommonComponents,
    Background: props => CommonComponents.Background({
        ...props, style: { backgroundColor: '#f9edcc', ...props.style }
    }),

    ThemedText: props => CommonComponents.ThemedText({
        ...props, style: { color: 'black', ...props.style }
    }),
    
    BackButton: props => CommonComponents.BackButton({
        ...props, style: { button: tw`bg-[rgba(237,174,73,1)]`, iconColor: 'black' }
    }),

    SmallButton: props => CommonComponents.SmallButton({
        ...props, style: { button: tw`bg-[rgba(237,174,73,1)]`, text: tw`text-black` }
    }),

    Section: props => CommonComponents.Section({
        ...props,
        style: {container: tw`bg-[rgba(249,223,116,1)]`,title: tw`text-black`,description: tw`text-gray-800` }
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
        ...props, style: { ...tw`bg-[rgba(249,223,116,1)]`, textColor: 'black', iconColor: 'black', ...props.style }
    }),
};

export { DarkThemeComponents, LightThemeComponents };
