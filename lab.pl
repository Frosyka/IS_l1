ingredient(мука).
ingredient(яйца).
ingredient(мясо).  
ingredient(картошка).  
ingredient(рис).     
ingredient(овощи). 
ingredient(паста).    
ingredient(сыр).
ingredient(сахар).   
ingredient(духовка).      
ingredient(рыба).     
ingredient(лимон).       
ingredient(помидор).   
ingredient(огурец).  
ingredient(курица).  
ingredient(специи).  
ingredient(хлеб).  
ingredient(молоко).   
ingredient(хлопья).  
ingredient(вода).     
ingredient(чайные_листья).

recipe(блинчики) :- 
    ingredient(мука), ingredient(яйца).
recipe(веганский_плов) :- 
    ingredient(рис), ingredient(овощи).
recipe(запечённая_рыба) :- 
    ingredient(рыба), ingredient(лимон), ingredient(духовка).
recipe(овощной_салат) :- 
    ingredient(помидор), ingredient(огурец), \+ingredient(мясо).
recipe(завтрак_из_хлопьев) :- 
    ingredient(молоко), ingredient(хлопья).
recipe(чай) :- 
    ingredient(вода), ingredient(чайные_листья).

%recipe(блинчики)
%findall(Recipe, recipe(Recipe), Recipes)
%ingredient(мука)
%recipe(X)
%recipe(овощной_салат)
%recipe(_)
%findall(R, recipe(R), List)
%findall(R, (recipe(R), R \= чай), Recipes)
%findall(I, ingredient(I), List), length(List, N)
%findall(R, recipe(R), Recipes)
