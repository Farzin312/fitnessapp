import { StyleSheet, Dimensions } from 'react-native';

const { width } = Dimensions.get('window');

export default StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    width: width * 0.9, // 90% of screen width
    marginBottom: 10,
  },
  button: {
    width: width * 0.9, // 90% of screen width
    padding: 5,
    marginTop: 10,
  },
  link: {
    color: '#007bff',
    marginTop: 10,
  },
});
