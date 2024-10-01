#include<iostream>

int main(){
	float mark;
	std::cout<<"Enter the marks "<<std::endl;
	std::cin>>mark;
	if(mark<=25){
		std::cout<<"F";
	}
	else if(mark<=44){
		std::cout<<"E";
	}
	else if(mark<=49){
		std::cout<<"D";
	}
	else if(mark<=59){
		std::cout<<"C";
	}
	else if(mark<=79){
		std::cout<<"B";
	}
	else if(mark<=100){
		std::cout<<"A";
	}
}
