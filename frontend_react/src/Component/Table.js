import { Table } from 'antd';
import axios from 'axios';
import { useState, useEffect } from 'react';


const Tab = ({ company, location, level, tag }) => {
  const [table, setTable] = useState([])
  const [loading, setLoading] = useState(true)
  useEffect(() => {
      console.log(company)
      console.log(location)
      console.log(level)
      console.log(tag)
    axios.post('http://127.0.0.1:8000/search', {
      "company": company,
      "location": location,
      "level": level,
      "tag": tag
    })
    .then((res) => { 
      setTable(res.data)
      console.log(res.data)
      setLoading(false)
    })
    .catch((error) => { console.log(error) })
  },[company, location, level, tag])

  const columns = [
    {
      title: 'Company',
      dataIndex: ['company', 'company'],
    },
    {
        title: 'Icon',
        dataIndex: ['company', 'icon_url'],
        render: theImageURL => <img alt={theImageURL} src={theImageURL} />
    },
    {
      title: 'Location',
      dataIndex: 'location',
    },
    {
      title: 'Level',
      dataIndex: 'level',
    },
    {
        title: 'Years Of Experience (yrs)',
        dataIndex: 'yearsofexperience',
    },
    {
      title: 'Tag',
      dataIndex: 'tag',
    },
    {
      title: 'Base Salary ($K USD)',
      dataIndex: 'base_salary',
    },
    {
        title: 'Stock Grant Value ($K USD)',
        dataIndex: 'stockgrantvalue',
    },
    {
        title: 'Bonus ($K USD)',
        dataIndex: 'bonus',
    },
    {
      title: 'Total Yearly Compensation($K USD)',
      dataIndex: 'totalyearlycompensation'
    },
    {
      title: 'Remote?',
      dataIndex: 'remote',
      render: remote => (remote? <p>Yes</p>:<p>No</p>)
    },
  ];
  
  
  return (loading?<h1>Loading...</h1>:<Table columns={columns} dataSource={table} />)
}

export default Tab