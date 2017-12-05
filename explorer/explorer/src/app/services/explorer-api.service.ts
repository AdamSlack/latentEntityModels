import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import 'rxjs/add/operator/toPromise';
import {Observable, Subject} from 'rxjs';

@Injectable()
export class ExplorerApiService {

  constructor(private http: HttpClient) { }
  
    public ROOT : string = 'http://grapesoda.hopto.org:8080/api/';
  
    public requestEntities(book_title: string) : Observable<any> {
      // example... 'http://localhost:8080/stockbroker?stockID=AMG&granularity=TIME_SERIES_DAILY'
      let url =  this.ROOT + 'books/' + book_title;
      console.log(url);
  
      return this.http.get(url);
    }

    public requestEntityTerms(book_title: string, entity : string) : Observable<any> {
      // example... 'http://localhost:8080/stockbroker?stockID=AMG&granularity=TIME_SERIES_DAILY'
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
      console.log('url');
      return this.http.get(url);
    }

    public requestTopicTerms(topicID : number) : Observable<any>{
      let url = this.ROOT + 'topics/' + topicID.toString();
      console.log('url')
      return this.http.get(url);
    }
}
