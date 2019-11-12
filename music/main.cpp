//
//  main.cpp
//  music
//
//  Created by Young kyg Lee on 27/08/2019.
//  Copyright © 2019 YoungQ. All rights reserved.
//

#include<iostream>
#include<fstream>
#include<string>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::string in_line;
    std::ifstream in("t1.wav");
    printf("12");
    while(getline(in,in_line)){
        printf("1");
        std::cout<<in_line<<std::endl;
    }
    in.close();
}
