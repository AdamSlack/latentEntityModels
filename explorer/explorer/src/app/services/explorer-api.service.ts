import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import 'rxjs/add/operator/toPromise';
import {Observable, Subject} from 'rxjs';

@Injectable()
export class ExplorerApiService {

  constructor(private http: HttpClient) { }
  
    public ROOT : string = 'http://localhost:8081';
  
    public requestEntities(book_title: string) : Observable<any> {
      // example... 'http://localhost:8080/stockbroker?stockID=AMG&granularity=TIME_SERIES_DAILY'
      let url =  this.ROOT + '/books/' + book_title;
      console.log('url');
  
      return this.http.get(url);
    }

    public requestEntityTerms(book_title: string, entity : string) : Observable<any> {
      // example... 'http://localhost:8080/stockbroker?stockID=AMG&granularity=TIME_SERIES_DAILY'
      let url =  this.ROOT + '/books/' + book_title + '/entities/' + entity;
      console.log('url');
  
      return this.http.get(url);
    }

  
}
