import { Select } from 'antd';
import 'antd/dist/antd.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

const { Option } = Select;

const Companies = ({ setCompany, setCheck }) => {

    const [companies, setCompanies] = useState([])
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/company/')
        .then((res) => { 
          //console.log(res.data);
          setCompanies(res.data)
          //console.log(companies);
        })
        .catch((error) => { console.log(error) })
    },[])

    const onChange = (value) => {
        console.log(`selected ${value}`);
        //console.log(companies);
        setCompany(value)
        setCheck(false)
      }
      
    const onSearch = (val) => {
        console.log('search:', val);
      }
      
      return(
        <Select
          showSearch
          style={{ width: 200 }}
          defaultValue={null}
          onChange={onChange}
          onSearch={onSearch}
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
        <Option value={null}>{"All"}</Option>
        {companies.map((company)=>{
            return <Option value={company['company_name']}>{company['company_name']}</Option>
        })}  
        </Select>
      );

}



export default Companies