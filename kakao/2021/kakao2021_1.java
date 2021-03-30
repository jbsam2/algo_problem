class Solution {
  public String solution(String new_id) {
      String tmp = new_id.toLowerCase();
      
      tmp = tmp.replaceAll("[^a-z0-9-_.]","");
      tmp = tmp.replaceAll("[.]{2,}",".");
      tmp = tmp.replaceAll("^[.]|[.]$","");
      if(tmp.equals(""))
          tmp+="a";
      if(tmp.length() > 15)
      {
          tmp = tmp.substring(0,15);
          tmp = tmp.replaceAll("^[.]|[.]$","");
      }
      if(tmp.length() < 3)
      {
          while(tmp.length()<3)
              tmp += tmp.charAt(tmp.length()-1);
      }               
      return tmp;
  }
}