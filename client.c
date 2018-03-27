#include <stdlib.h>
#include <stdio.h>
#include <string.h>
//#include <weeve_sockets.h>

int main( int argc, char *argv[] ) 
{
	//on which topic you want send your data?
	char topic[16];
	sscanf(argv[1],"%s", topic);

	int topic_len = strlen(topic);

	//the your hex-coded data
    unsigned char str[150];

	printf("Reading data stream\n");
	scanf("%s", str);
	
	printf("%s\n", topic);
	printf("%s\n", str);	
	//set your price and how many datasets you want to trade with
	//int price = 50;
	//int amount = 1;


	//float b = 0.0f;
	//float c = 0.0f;
	//float d = 0.0f;

	// Beware argv[0] is program name
	//sscanf(argv[1],"%f", &a);
	//sscanf(argv[2],"%f", &b);
	//sscanf(argv[3],"%f", &c);
	//sscanf(argv[4],"%f", &d);
	//printf("%s", argv[1]);

	//printf("a is: %f\n", a);
	//printf("b is: %f\n", b);
	//printf("c is: %f\n", c);
	//printf("d is: %f\n", d);

	//float abcd[4] = { a, b, c, d };

	//char *data = malloc(sizeof(float) * 4);
	//u_int8_t *float_data = (u_int8_t*) &abcd;
	
	// int i;
	// for(i=0;i<4;i++)
	// {
	// //producer(topic, topic_len, price, amount, data, data_len);
	    /*set strH with nulls*/

	return 0;
}