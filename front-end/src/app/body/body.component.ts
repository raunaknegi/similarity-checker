import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-body',
  templateUrl: './body.component.html',
  styleUrls: ['./body.component.css']
})
export class BodyComponent implements OnInit {

  constructor(private http:HttpClient) { }

  Score:Number=-1;
  doc1:string="";
  doc2:string="";
  modelName:string="BERT";
  error:boolean=false;
  errorMessage:string="";
  loading:boolean=false;

  ngOnInit(): void {
  }

  getScore(){
    this.loading=true;
    if(!this.doc1 || !this.doc2){
      this.error=true;
      this.errorMessage="Please enter the values for the documents";    
    }else{
      var object={
        doc1:this.doc1,
        doc2:this.doc2,
        modelName:this.modelName
      }
      this.SendData(object);      
    }
  }

  SendData(json_object:any){
    this.http.post("http://127.0.0.1:5000/predict",json_object).subscribe((response:any)=>{
      this.Score=response['similarity'];
      console.log(response);
      this.loading=false;
    });
  }

}
