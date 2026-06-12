import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
} from 'react-native';

export default function App() {

  const [count, setCount] = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleDecrement = () => {
    if (count > 0) {
      setCount(count - 1);
    }
  };

  const handleReset = () => {
    setCount(0);
  };

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <View
      style={[
        styles.container,
        {
          backgroundColor: isDarkMode ? '#121212' : '#ffffff',
        },
      ]}
    >

      <Text
        style={[
          styles.title,
          {
            color: isDarkMode ? '#ffffff' : '#000000',
          },
        ]}
      >
        Digital Counter
      </Text>

      <Text
        style={[
          styles.counter,
          {
            color: isDarkMode ? '#ffffff' : '#000000',
          },
        ]}
      >
        {count}
      </Text>

      <View style={styles.buttonRow}>

        <TouchableOpacity
          style={styles.button}
          onPress={handleIncrement}
        >
          <Text style={styles.buttonText}>
            Increment
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.button}
          onPress={handleDecrement}
        >
          <Text style={styles.buttonText}>
            Decrement
          </Text>
        </TouchableOpacity>

      </View>

      <TouchableOpacity
        style={styles.resetButton}
        onPress={handleReset}
      >
        <Text style={styles.buttonText}>
          Reset
        </Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.themeButton}
        onPress={toggleTheme}
      >
        <Text style={styles.buttonText}>
          Toggle Theme
        </Text>
      </TouchableOpacity>

    </View>
  );
}

const styles = StyleSheet.create({

  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },

  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 20,
  },

  counter: {
    fontSize: 60,
    fontWeight: 'bold',
    marginBottom: 40,
  },

  buttonRow: {
    flexDirection: 'row',
    marginBottom: 20,
  },

  button: {
    backgroundColor: '#3498db',
    padding: 15,
    borderRadius: 10,
    marginHorizontal: 10,
  },

  resetButton: {
    backgroundColor: '#e67e22',
    padding: 15,
    borderRadius: 10,
    marginBottom: 20,
  },

  themeButton: {
    backgroundColor: '#27ae60',
    padding: 15,
    borderRadius: 10,
  },

  buttonText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: 'bold',
  },

});