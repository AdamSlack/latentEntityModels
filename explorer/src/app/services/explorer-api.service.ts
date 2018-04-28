import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import 'rxjs/add/operator/toPromise';
import {Observable, Subject} from 'rxjs';

@Injectable()
export class ExplorerApiService {

  constructor(private http: HttpClient) { }
  
    public ROOT : string = 'http://localhost:8000/api/';
  
    public requestEntities(book_title: string) : Observable<any> {
      let url =  this.ROOT + 'books/' + book_title;
      console.log(url);
  
      return this.http.get(url);
    }

    public requestEntityTerms(book_title: string, entity : string) : Observable<any> {
      let url =  this.ROOT + 'books/' + book_title + '/entities/' + entity;
      console.log(url);
  
      return this.http.get(url);
    }

    public requestBookTopics(book_title: string) : Observable<any> {
      let url = this.ROOT + 'books/' + book_title + '/topics'
      console.log(url);
      return this.http.get(url);
    }

    public requestBookTitles() : Observable<any> {
      let url = this.ROOT + 'books';
      console.log(url)
      return this.http.get(url);
    }

    public requestTopicIDs() : Observable<any> {
      let url = this.ROOT + 'topics';
      console.log(url)
      return this.http.get(url);
    }

    public requestTopicTerms(topicID : number) : Observable<any>{
      let url = this.ROOT + 'topics/' + topicID.toString();
      console.log(url)
      return this.http.get(url);
    }

    public requestEntityTopics(bookTitle: string, entityName: string) : Observable<{
      topics : Array<{
        entity: string,
        book:string,
        topicID:number,
        strength:number
      }>
    }>{
      let url = this.ROOT + 'topics/' + bookTitle + '/' + entityName;
      console.log(url);
      return this.http.get<{
        topics : Array<{
          entity: string,
          book:string,
          topicID:number,
          strength:number
        }>
      }>(url);
    }

    public requestLatentEntities(n_entities = 5) : Observable<{latent_entities : Array<Array<number>>}>{
      let url = this.ROOT + 'latent_entities?number=' + n_entities;
      console.log(url);
      return this.http.get<{latent_entities : Array<Array<number>>}>(url);
    }
}

