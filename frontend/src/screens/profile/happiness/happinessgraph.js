import React from 'react';
import { Dimensions, View } from 'react-native';
import { Svg, Path } from 'react-native-svg';
import * as d3 from 'd3-scale';
import { line, curveNatural } from 'd3-shape';

const HappinessGraph = ({ data }) => {
    const svgWidth = Dimensions.get('window').width - 40;
    const svgHeight = 200;

    const scaleX = d3.scaleLinear()
        .domain([0, data.length - 1])
        .range([20, svgWidth - 20]);

    const scaleY = d3.scaleLinear()
        .domain([1, 100])  
        .range([svgHeight - 20, 20]);

    const lineGenerator = line()
        .x((_, index) => scaleX(index))
        .y(d => scaleY(d.rating))
        .curve(curveNatural);

    const pathData = lineGenerator(data);

    return (
        <View>
            <Svg height={svgHeight} width={svgWidth}>
                <Path d={pathData} stroke="blue" fill="none" strokeWidth={2} />
            </Svg>
        </View>
    );
};

export default HappinessGraph;
