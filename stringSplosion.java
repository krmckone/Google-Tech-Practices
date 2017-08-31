/* Author: Kaleb Robert McKone
 Creates a "string splosion" based on input string
stringSplosion("Code") = "CCoCodCode"
stringSplosion("abc") = "aababc"
stringSplosion("ab") = "aab"
*/

public String stringSplosion(String str) {
  String builder = "";
  int limit = 1;
  
  while(limit <= str.length()){
    for(int i = 0; i < limit; i++){
      builder = builder.concat(Character.toString(str.charAt(i)));
    }
  limit++;
  }
  return builder;
}
