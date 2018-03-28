#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <weeve_sockets.h>

int main( int argc, char *argv[] ) 
{
	//on which topic you want send your data?
	char topic[16];
	sscanf(argv[1],"%s", topic);
	int topic_len = sizeof(topic);

	//the your hex-coded data
    unsigned char str[256];
	printf("Reading data stream\n");
	scanf("%s", str);

	// Print for now
	printf("%s\n", topic);
	printf("%s\n", str);	
	int price = 5;
	int amount = 1;

	producer(topic, topic_len, price, amount, str, sizeof(str));

	return 0;
}